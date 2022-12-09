#!/usr/bin/perl
# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5
# J.Christensen 05Dec2022

use v5.24;
use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(utf8)';
binmode STDERR, ':encoding(utf8)';
say "\n---- PERL $0 ----";

# read the input, strip newlines
chomp(my @lines = <<>>);

say "The top crates for Part One are: " . moveCrates(@lines, 9000);
say "The top crates for Part Two are: " . moveCrates(@lines, 9001);

sub moveCrates {
    my $craneModel = pop(@_);
    my (@lines) = @_;

    # determine number of stacks, and height of tallest stack
    my $height = 0;
    my $nstack = 0;
    foreach (@lines) {
        my (@f) = split;
        #say @f;
        if ($f[0] eq "1") {
            $nstack = $f[-1];
            last
        }
        $height += 1;
    }
    #say "$height $nstack";

    # build the stacks
    my @stacks = ();
    for (0..$nstack-1) {
        push( @stacks, [()] );
    }

    for (my $l=$height-1; $l>=0; $l--) {
        for (my $s=0; $s<$nstack; $s++) {
            my $charIndex = $s * 4 + 1;
            my $crate = substr($lines[$l], $charIndex, 1);
            if ($crate ne ' ') {
                #say "push $crate onto stack $s";
                push( @{$stacks[$s]}, $crate );
            }
        }
    }

    # start up the crane
    foreach (@lines) {
        if (substr($_, 0, 4) eq "move") {
            my ($ignore1, $n, $ignore2, $src, $ignore3, $dest) = split;
            # elves index the stacks from one not zero, so subtract 1
            $src--;
            $dest--;
            if ($craneModel == 9000) {
                for (0..$n-1) {
                    my $crate = pop( @{$stacks[$src]} );
                    push( @{$stacks[$dest]}, $crate );
                }
            }
            elsif ($craneModel == 9001) {
                my @crates = ();
                for (0..$n-1) {
                    unshift ( @crates, pop( @{$stacks[$src]} ));
                }
                push( @{$stacks[$dest]}, @crates );
            }
            else {
                die "Invalid crane model: $craneModel\n";
            }
        }
    }

    # print the stacks
    #for (0..$nstack-1) {
    #    say @{$stacks[$_]};
    #}

    my $topcrates = "";
    for (0..$nstack-1) {
        $topcrates .= $stacks[$_][-1];
    }
    $topcrates;
}
