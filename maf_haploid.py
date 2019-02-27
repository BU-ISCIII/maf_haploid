#!/usr/bin/env python

import vcf
import argparse

parser = argparse.ArgumentParser(description='Parse vcf file from GATK and calculate MAF for haploid organism')
parser.add_argument('-f','--file', required=True,
                        help='vcf v4.1 file with haploid genotypes')

args = parser.parse_args(['-f', '../data/all_variants.vcf'])

vcf_reader = vcf.Reader(open(args.file, 'r'), strict_whitespace=True)

for record in vcf_reader:
    print(record.CHROM)
