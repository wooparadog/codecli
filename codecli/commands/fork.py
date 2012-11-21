import os
from subprocess import check_call
from contextlib import contextmanager
from getpass import getuser

def populate_argument_parser(parser):
    username = getuser()
    parser.add_argument('upstream', help="name of upstream repo [e.g. dae]")
    parser.add_argument('origin', help="name of my fork [e.g. dae_hongqn]")
    parser.add_argument('--username', default=username,
                        help="douban unified account name [default: %(default)s]")


def main(args):
    name = args.upstream
    check_call(['git', 'clone', git_url(args.origin), name])
    with cd(name):
        check_call(['git', 'remote', 'add', 'upstream', git_url(name)])
        check_call(['git', 'config', 'user.email',
                    '%s@douban.com' % args.username])
        check_call(['git', 'config', 'user.name', args.username])

def git_url(repo_name):
    return 'http://code.dapps.douban.com/%s.git' % repo_name


@contextmanager
def cd(path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield cwd
    finally:
        os.chdir(cwd)
