load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "talking_containers_lib",
    srcs = glob(["*.py"]),
    deps = ["//config:config_handler"],
)

py_library(
    name = "some_other_lib",
    srcs = glob(["*.py"]),
    deps = ["//config:config_handler"],
)
