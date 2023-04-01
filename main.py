from auth import authorisation
from parsers.groups_parser import groups_parser
from parsers.posts_parser import posts_parser

if __name__ == '__main__':
    posts_parser(authorisation())
    groups_parser(authorisation())
