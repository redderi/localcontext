import argparse


class Parser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser(prog="localcontext",
                                                description="utils for get project local context",
                                                allow_abbrev=False)
        self._setup_arguments()

    def _setup_arguments(self):
        self.__parser.add_argument(
            "-t", "--tree",
            action="store_true",
            help="print project tree"
        )
        self.__parser.add_argument(
            "-s", "--system",
            action="store_true",
            help="print system information"
        )
        self.__parser.add_argument(
            "-f", "--filename",
            action="store",
            help="set output filename"
        )
        self.__parser.add_argument(
            "-n", "--number",
            action="store",
            help="print line number in code"
        )
        self.__parser.add_argument(
            "-e", "--exclude",
            nargs="+",          
            help="list of files or directories to skip"
        )

    def parse(self):
        args = self.__parser.parse_args()
        return {
            "tree": args.tree,
            "system": args.system, 
            "number": args.number,
            "filename": args.filename,
            "exclude": args.exclude or []  
        }
