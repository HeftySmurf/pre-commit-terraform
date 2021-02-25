import argparse
import os
import subprocess
import sys

def log_msg(msg=None):
    print("VERBOSE:{0}".format(msg))

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="""Run terraform-docs on a set of files. Follows the standard convention of
                       pulling the documentation from main.tf in order to replace the entire
                       README.md file each time."""
    )
    parser.add_argument(
        '--hide', dest='hide',
        help='hide section [header, inputs, modules, outputs, providers, requirements, resources]'
    ),
    parser.add_argument(
        '--show', dest='show',
        help='show section [header, inputs, modules, outputs, providers, requirements, resources]'
    ),
    parser.add_argument(
        '--dest', dest='dest', default='README.md',
    )
    parser.add_argument(
        '--sort-by-required', dest='sort', action='store_true',
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    dirs = []
    for filename in args.filenames:
        if (os.path.realpath(filename) not in dirs and \
                (filename.endswith(".tf") or filename.endswith(".tfvars"))):
            dirs.append(os.path.dirname(filename))

    retval = 0

    for dir in dirs:
        try:
            procArgs = []
            procArgs.append('terraform-docs')
            if args.sort:
                procArgs.append('--sort-by-required')
            procArgs.append('md')
            procArgs.append("./{dir}".format(dir=dir))
            if args.hide != None:
                procArgs.append('--hide \'{sections}\''.format(sections=",".join(args.hide)))
            procArgs.append("| sed -e '$ d' -e 'N;/^\\n$/D;P;D'")
            procArgs.append('>')
            procArgs.append("./{dir}/{dest}".format(dir=dir,dest=args.dest))
            log_msg(" ".join(procArgs))
            subprocess.check_call(" ".join(procArgs), shell=True)
        except subprocess.CalledProcessError as e:
            print(e)
            retval = 1
    log_msg("retval:{0}".format(retval))
    return retval


if __name__ == '__main__':
    sys.exit(main())