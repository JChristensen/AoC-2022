#!/usr/bin/perl
# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4
# J.Christensen 04Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
use List::Util qw(min max);
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';
say "\n---- PERL $0 ----";

# read the input, strip newlines
chomp(my @lines = <<>>);

#---- PART ONE ----#
my $total = 0;
foreach (@lines) {
    my ($f1, $f2, $f3, $f4) = split/,|-/;
    my $min1 = min($f1, $f2);
    my $max1 = max($f1, $f2);
    my $min2 = min($f3, $f4);
    my $max2 = max($f3, $f4);
    if ( (($min1 >= $min2) && ($max1 <= $max2)) || (($min2 >= $min1) && ($max2 <= $max1)) ) {
        $total++;
    }
}
say "Part 1 total $total.";

#---- PART TWO ----#
$total = 0;
foreach (@lines) {
    my ($f1, $f2, $f3, $f4) = split/,|-/;
    my $min1 = min($f1, $f2);
    my $max1 = max($f1, $f2);
    my $min2 = min($f3, $f4);
    my $max2 = max($f3, $f4);
    if ( (($max1 >= $min2) && ($max1 <= $max2)) || (($max2 >= $min1) && ($max2 <= $max1)) ) {
        $total++;
    }
}
say "Part 2 total $total.";
