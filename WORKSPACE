workspace(name = "rules_python_dup_test")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "bazel_skylib",
    sha256 = "cd55a062e763b9349921f0f5db8c3933288dc8ba4f76dd9416aac68acee3cb94",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.5.0/bazel-skylib-1.5.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.5.0/bazel-skylib-1.5.0.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
SHA="c68bdc4fbec25de5b5493b8819cfc877c4ea299c0dcb15c244c5a00208cde311"
VERSION="0.31.0"
http_archive(
    name = "rules_python",
    sha256 = SHA,
    strip_prefix = "rules_python-{}".format(VERSION),
    url = "https://github.com/bazelbuild/rules_python/releases/download/{}/rules_python-{}.tar.gz".format(VERSION,VERSION),
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:pip.bzl", "pip_parse")
pip_parse(
    name = "my_requirements",
    requirements_lock = "//:requirements.txt",
)
# NOTE:  It would be nice to think that the following should work:
#    experimental_requirement_cycles = {
#        "nvidia": [
#            "nvidia_cublas_cu11", "nvidia_cuda_cupti_cu11"
#        ]
#    }
# However if you add it you will see that it makes things worse, not better.

load("@my_requirements//:requirements.bzl", "install_deps")
install_deps()
