set -e

# --------------------------------------------------------------
# Text files under /sandbox are automatically returned...
source ~/cyber_dojo_fs_cleaners.sh
export REPORT_DIR=${CYBER_DOJO_SANDBOX}/report
function cyber_dojo_enter()
{
  # 1. Only return _newly_ generated reports.
  cyber_dojo_reset_dirs ${REPORT_DIR}
}
function cyber_dojo_exit()
{
  # 2. Remove text files we don't want returned.
  cyber_dojo_delete_dirs .pytest_cache
  #cyber_dojo_delete_files ...
}
cyber_dojo_enter
trap cyber_dojo_exit EXIT SIGTERM

# --------------------------------------------------------------
# mypy spends most of its time on typeshed's stubs for the standard library
# rather than on anything you wrote, and that work is the same on every test-run.
# The image holds it already analysed; this says where. Left to itself mypy
# would use .mypy_cache here in the sandbox, which starts empty every run.
export MYPY_CACHE_DIR=/mypy-cache

# coverage watches your code through sys.monitoring rather than by a callback
# on every line, which is a good deal cheaper. The numbers it reports are the
# same either way.
export COVERAGE_CORE=sysmon

# Python puts a script's own directory first on the import path, so a test in
# a sub-directory would look for its source file beside itself. Naming the
# sandbox is what lets such a test import a source file in the root.
export PYTHONPATH=${CYBER_DOJO_SANDBOX}
# --------------------------------------------------------------

echo MyPy
mypy *.py | tee ${REPORT_DIR}/mypy.txt || true

# Each test file is run in turn, so a second test file is not silently left
# out. [coverage run] takes one script and treats any later name as an
# argument to it, so naming them all on one line would run only the first.
# --append is what gathers the separate runs into a single report below.
echo
for test_file in $(find . -name '*test*.py' | sort); do
  coverage run \
    --append \
    --source=${CYBER_DOJO_SANDBOX} \
      "${test_file}"
done

# https://coverage.readthedocs.io
echo
coverage report \
  --show-missing \
  | tee ${REPORT_DIR}/coverage.txt

# http://pycodestyle.pycqa.org/en/latest/intro.html#configuration
echo
pycodestyle ${CYBER_DOJO_SANDBOX} \
  --show-source `# show source code for each error` \
  --show-pep8   `# show relevant text from pep8` \
  --ignore E302,E305,W293 \
  --max-line-length=80 \
  > ${REPORT_DIR}/style.txt

# E302 expected 2 blank lines, found 0
# E305 expected 2 blank lines after end of function or class
# W293 blank line contains whitespace
