package main

import (
	"context"
	"fmt"
	"log"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
	// Load AWS config (uses credentials from env or ~/.aws/)
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		log.Fatalf("Unable to load SDK config, %v", err)
	}

	// Create S3 client
	client := s3.NewFromConfig(cfg)

	// List buckets
	result, err := client.ListBuckets(context.TODO(), &s3.ListBucketsInput{})
	if err != nil {
		log.Fatalf("Unable to list buckets, %v", err)
	}

	fmt.Println("Buckets:")
	for _, bucket := range result.Buckets {
		fmt.Printf(" - %s (created on: %s)\n", aws.ToString(bucket.Name), bucket.CreationDate)
	}
}
