#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import shutil
# from dateutil import parser
from paddleocr import PaddleOCR
import shell_execute

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser(description='ocreval tools')
    args_parser.add_argument('--action',  action='store', dest='action', default='copy_tifs')
    args_parser.add_argument('--ds-dir',  action='store', dest='ds_dir', default='')
    args_parser.add_argument('--ocr-name',  action='store', dest='ocr_name', default='paddleocr')
    args = args_parser.parse_args()
    print(args)

    pages = os.path.join(args.ds_dir, 'pages')
    print(pages)

    f = open(pages,'r')
    pages_content = f.readlines()
    f.close()
    
    if args.action == 'prepare':
        #copy tif files to ./tif-files
        for line in pages_content:
            line_split = line.split(' ')
            #print(line_split)
            src = os.path.join(args.ds_dir, line_split[1].replace('\n', ''), line_split[0] + '.tif')
            dst = os.path.join('.', 'tif-files', line_split[0] + '.tif')
            shutil.copyfile(src, dst)


    if args.action == 'paddleocr':
        ocr = PaddleOCR(use_angle_cls=True, lang="en") # need to run only once to download and load model into memory
        for line in pages_content:
            line_split = line.split(' ')
            tif_file = os.path.join(args.ds_dir, line_split[1].replace('\n', ''), line_split[0] + '.tif')
            result = ocr.ocr(tif_file, cls=True)
            ocr_result = []
            for line in result:
                print(line)
                ocr_result.append(line[1][0] + '\n')
            
            output_file = os.path.join('.', 'paddleocr-output', line_split[0] + '.txt')
            if os.path.exists(output_file):
                os.unlink(output_file)

            f = open(output_file,'w')
            f.writelines(ocr_result)
            f.close()
            
            print('save to %s' % output_file)

            # generator accuracy report, save as to ./paddleocr-characters-acc/
            correct_file = os.path.join(args.ds_dir, line_split[1].replace('\n', ''), line_split[0] + '.txt')
            accuracy_report = os.path.join('.', 'paddleocr-accuracy', line_split[0] + '.txt')
            cmd = 'accuracy %s %s %s' % (correct_file, output_file, accuracy_report)
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            shell_execute.run(cmd, print_to_console=True)

            # generator wordsacc report, save as to ./paddleocr-words-acc/
            accuracy_report = os.path.join('.', 'paddleocr-wordacc', line_split[0] + '.txt')
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            cmd = 'wordacc %s %s %s' % (correct_file, output_file, accuracy_report)
            shell_execute.run(cmd, print_to_console=True)

    if args.action == 'ymocr':
         for line in pages_content:
            line_split = line.split(' ')
            output_file = os.path.join('.', 'ymocr-output', line_split[0] + '.txt')

            # generator accuracy report, save as to ./ymocr-characters-acc/
            correct_file = os.path.join(args.ds_dir, line_split[1].replace('\n', ''), line_split[0] + '.txt')
            accuracy_report = os.path.join('.', 'ymocr-accuracy', line_split[0] + '.txt')
            cmd = 'accuracy %s %s %s' % (correct_file, output_file, accuracy_report)
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            shell_execute.run(cmd, print_to_console=True)

            # generator wordsacc report, save as to ./ymocr-words-acc/
            accuracy_report = os.path.join('.', 'ymocr-wordacc', line_split[0] + '.txt')
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            cmd = 'wordacc %s %s %s' % (correct_file, output_file, accuracy_report)
            shell_execute.run(cmd, print_to_console=True)
    
    if args.action == 'abbyyocr':
         for line in pages_content:
            line_split = line.split(' ')
            output_file = os.path.join('.', 'abbyy-output', line_split[0] + '.txt')

            correct_file = os.path.join(args.ds_dir, line_split[1].replace('\n', ''), line_split[0] + '.txt')
            accuracy_report = os.path.join('.', 'abbyy-accuracy', line_split[0] + '.txt')
            cmd = 'accuracy %s %s %s' % (correct_file, output_file, accuracy_report)
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            shell_execute.run(cmd, print_to_console=True)

            accuracy_report = os.path.join('.', 'abbyy-wordacc', line_split[0] + '.txt')
            if os.path.exists(accuracy_report):
                os.unlink(accuracy_report)
            cmd = 'wordacc %s %s %s' % (correct_file, output_file, accuracy_report)
            shell_execute.run(cmd, print_to_console=True)

    if args.action == 'ocreval':
        cmd = 'accsum'
        for line in pages_content:
            line_split = line.split(' ')
            accuracy_report = os.path.join('.', '%s-accuracy' % args.ocr_name, line_split[0] + '.txt')
            cmd += ' %s' % accuracy_report
        cmd +=  ' >' + os.path.join('.', '%s-accuracy' % args.ocr_name, 'accuracy-report.txt')
        # print(cmd)
        shell_execute.run(cmd, print_to_console=True)

        cmd = 'accci'
        for line in pages_content:
            line_split = line.split(' ')
            accuracy_report = os.path.join('.', '%s-accuracy'  % args.ocr_name, line_split[0] + '.txt')
            cmd += ' %s' % accuracy_report
        cmd +=  ' >' + os.path.join('.', '%s-accuracy'  % args.ocr_name, 'accci-report.txt')
        # print(cmd)
        shell_execute.run(cmd, print_to_console=True)

        cmd = 'wordaccsum'
        for line in pages_content:
            line_split = line.split(' ')
            accuracy_report = os.path.join('.', '%s-wordacc' % args.ocr_name, line_split[0] + '.txt')
            cmd += ' %s' % accuracy_report
        cmd +=  ' >' + os.path.join('.', '%s-wordacc' % args.ocr_name, 'wordaccsum-report.txt')
        # print(cmd)
        shell_execute.run(cmd, print_to_console=True)
    
    sys.exit(0)
