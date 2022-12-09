#!/usr/bin/perl
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
# J.Christensen 06Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';
say "\n---- PERL $0 ----";

# read the input, strip newlines
chomp(my $buf = <<>>);

say "Part One: " . search($buf, 4);
say "Part Two: " . search($buf, 14);

# given string s, returns the position of the first substring of
# length n where all the characters in the substring are different.
sub search {
    my ($s, $n) = @_;

    for my $i (0..length($s) - $n) {
        my $sss = substr($s, $i, $n);
        my %d = ();
        for my $c (0..$n) {
            my $ch = substr($sss, $c, 1);
            if (exists $d{$ch}) { $d{$ch} += 1 }
            else { $d{$ch} = 1 }
        }
        my @k = keys %d;
        if ($#k == $n) {return $i + $n}
    }
}
