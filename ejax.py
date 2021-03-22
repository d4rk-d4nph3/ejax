########################################################################################
# Author:       d4rk-d4nph3
# Description:  Windows EVTX to JSON and XML converter
# Version:      0.1
# Modified at:  2021/03/22
########################################################################################

import json

import Evtx.Evtx as evtx
import xmltodict

def convert_to_json(input_evtx):
    with evtx.Evtx(input_evtx) as logs:
        for record in logs.records():
            log = ''
            log = log + record.xml()
            json_log = json.dumps(xmltodict.parse(log))
            print(json_log)

def convert_to_xml(input_evtx):
    with evtx.Evtx(input_evtx) as logs:
        for record in logs.records():
            print(record.xml())


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert a binary EVTX file into XML or JSON.")
    parser.add_argument("evtx", type=str,
                        help="Path to the Windows EVTX event log file")
    parser.add_argument("-m", type=str,
                        help="Conversion mode | either JSON or XML")
    args = parser.parse_args()

    if args.m == 'json':
        convert_to_json(args.evtx)
    elif args.m == 'xml':
        convert_to_xml(args.evtx)
    else:
        print("Unknown mode supplied as argument")
        print("Please read help carefully!")
        exit()
    

if __name__ == "__main__":
    main()

