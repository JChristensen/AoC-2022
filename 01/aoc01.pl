#!/usr/bin/perl
# Advent of Code, Dec 01.
# https://adventofcode.com/2022/day/1
# J.Christensen 01Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';

my $cal = 0;        # total calories for current elf
my @elves = ();     # a list of total calories for all elves

while (<<>>) {
    chomp;
    # strip leading and trailing whitespace
    $_ =~ s/^\s+|\s+$//g;
    if (length($_) == 0) {
        push @elves, $cal;
        $cal = 0;
    }
    else {
        $cal += $_;
    }
}
if ($cal > 0) {push @elves, $cal}
my @sortedElves = sort {$b <=> $a} @elves;
my $topThree = $sortedElves[0] + $sortedElves[1] + $sortedElves[2];
say "There are ", $#elves + 1, " elves.";
say "The most calories an elf has is $sortedElves[0].";
say "The top three elves have a total of $topThree calories.";
