#!/usr/bin/perl
# Advent of Code, Dec 02, Part 1.
# https://adventofcode.com/2022/day/2
# J.Christensen 02Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';

# R=1 P=2 S=3 Win=6 Draw=3 Lose=6
my %score = ( "R R" => 1+3, "R P" => 2+6, "R S" => 3+0,
              "P R" => 1+0, "P P" => 2+3, "P S" => 3+6,
              "S R" => 1+6, "S P" => 2+0, "S S" => 3+3 );

say("\n----PERL----");
my $total = 0;
while (<<>>) {
    chomp;
    # strip leading and trailing whitespace
    $_ =~ s/^\s+|\s+$//g;
    my $round = $_;
    # change the letters to make more sense
    $round =~ tr/ABCXYZ/RPSRPS/;
    # look up the score
    my $points = $score{$round};
    # check to make sure the lookup worked
    if ($points) {
        #say("$_ $round $points");
        $total += $points;
    }
    else {
        die("Error: $round\n");
    }
}

say "The total score is $total.";
