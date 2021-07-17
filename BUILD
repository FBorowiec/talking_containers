load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_push")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "talking_containers_lib",
    srcs = glob(["src/*.py"]),
)

py_binary(
    name = "run_container",
    srcs = ["run_container.py"],
    deps = [":talking_containers_lib"],
)

container_image(
    name = "ubuntu_python3",
    base = "@ubuntu_python3//image",
)

py3_image(
    name = "talking_containers_image",
    srcs = ["run_container.py"],
    base = "ubuntu_python3",
    main = "run_container.py",
    deps = [":talking_containers_lib"],
)

container_push(
    name = "push_image",
    format = "Docker",
    image = "talking_containers_image",
    registry = "index.docker.io",
    repository = "nutshellhub/talking_container",
    tag = "latest",
)
