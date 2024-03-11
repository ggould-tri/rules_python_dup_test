# If fs.sshfs isn't present this fails.
import fs.sshfs

if __name__ == "__main__":
    from fs import open_fs
    # If the s3 provider isn't present this fails.
    s3fs = open_fs('s3://mybucket')
    print("Test passed.")
