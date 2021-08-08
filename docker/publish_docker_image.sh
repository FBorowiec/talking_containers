#!/usr/bin/env bash

set -e

IMG_TAG=$(<release.version)
echo "Release: $IMG_TAG"

echo "Building docker image.."
bazel run -c opt //:talking_containers_image -- --norun
echo "Docker image built successfully!"

echo "Pushing docker image.."
bazel run -c opt --define image_tag="${IMG_TAG}" //:push_image
echo "Docker image pushed successfully!"
