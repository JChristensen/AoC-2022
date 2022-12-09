#!/usr/bin/perl
# Advent of Code, Dec 02, Part 2.
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

# given the opponent's throw, this hash encodes whether we should
# play for win, lose or draw.
my %strategy = ( "R W" => "P", "R L" => "S", "R D" => "R",
                 "P W" => "S", "P L" => "R", "P D" => "P",
                 "S W" => "R", "S L" => "P", "S D" => "S" );

say("\n----PERL----");
my $total = 0;
while (<<>>) {
    chomp;
    # strip leading and trailing whitespace
    $_ =~ s/^\s+|\s+$//g;
    # determine what we should play
    my $round = $_;
    $round =~ tr/ABCXYZ/RPSLDW/;
    # replace the second code letter from the input with our throw
    my $throw = $strategy{$round};
    $round = substr($round, 0, 2) . $throw;
    # and figure the points as in part 1.
    my $points = $score{$round};
    # test to make sure the lookup worked
    if ($points) {
        #say("$_ $round $points $throw");
        $total += $points;
    }
    else {
        die("Error: $round\n");
    }
}

say "The total score is $total.";
