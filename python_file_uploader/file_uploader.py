from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    # client = Minio(
    #     "play.min.io",
    #     access_key="Q3AM3UQ867SPQQA43P2F",
    #     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    # )

    client = Minio(
        "127.0.0.1:9000",
        access_key="misr_admin",
        secret_key="misr_admin",
        secure=False
    )
    # Make 'misr' bucket if not exist.
    found = client.bucket_exists("misr")
    if not found:
        client.make_bucket("misr")
    else:
        print("Bucket 'misr' already exists")

    # Upload 'humans_test.jpeg.jpeg' as object name
    # 'asiaphotos-2015.zip' to bucket 'misr'.
    client.fput_object(
        "misr", "humans_test.jpeg", "humans_test.jpeg",
    )
    print(
        "'humans_test.jpeg.jpeg' is successfully uploaded as "
        "object 'humans_test.jpeg' to bucket 'misr'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
