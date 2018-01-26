import argparse
import time

known_drivers = ['local', 's3']

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are ".join(known_drivers) )
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = argparse.ArgumentParser(description="""
        Back up Databases locally or the cloud
    """)
    parser.add_argument('url', help="URL of database to backup")
    parser.add_argument('--driver', '-d',
                        help='how & where to store backup',
                        nargs=2,
                        metavar=("DRIVER", "DESTINATION"),
                        action=DriverAction,
                        required=True)
    return parser


def main():
    import boto3
    from dbbackup import mysqldump, pgdump, storage

    args = create_parser().parse_args()
    dump = mysqldump.dump(args.url)

    if args.drive == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print("Backing database up to %s to S3 as %s" % (args.destination, file_name))
        storage.s3(client, dump.stdout, args.destination, 'example.sql', file_name)
    else:
        outfile = open(args.destination, 'w')
        print("Backing database up locally to %s" % outfile.name)
        storage.local(dump.stdout, outfile)


