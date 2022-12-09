#!/usr/bin/perl
# Rucksack Reorganization
# Advent of Code, Dec 03.
# https://adventofcode.com/2022/day/3
# J.Christensen 03Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';

say "\n---- PERL $0 ----";

# read the input, strip newlines
chomp(my @lines = <<>>);

#---- PART ONE ----#
my $total = 0;
foreach (@lines) {
    # number of items in one compartment
    my $n = length($_) / 2;
    # make the first and second compartment lists
    my $c1 = substr($_, 0, $n);
    my $c2 = substr($_, $n);
    #say("$_ $c1 $c2");

    # find the duplicate item, calculate and accumulate the priority
    for (my $r=0; $r<$n; $r++) {
        my $item = substr($c1, $r, 1);
        if (index($c2, $item) >= 0) {
            $total += priority($item);
            last;
        }
    }
}
say "The sum of priorities for Part 1 is $total.";

#---- PART TWO ----#
$total = 0;
for (my $r=0; $r<$#lines; $r+=3) {                  # three elves at a time
    for (my $i=0; $i<length($lines[$r]); $i++) {    # iterate each character for the first elf
        my $item = substr($lines[$r], $i, 1);
        if (index($lines[$r+1], $item) >= 0 && index($lines[$r+2], $item) >= 0) {
            $total += priority($item);
            last;
        }
    }
}
say "The sum of priorities for Part 2 is $total.";
      
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
sub priority {
    my ($ch) = @_;
    ord($ch) > 96 ? ord($ch) - 96 : ord($ch) - 64 + 26;
}
