# End of support

The project on which this project depends, IBM Feedback Directed Program Restructuring, is no longer supported on Linux on Power. This project is being archived.

# Project Description

FDPR wrapper scripts

IBM's [Feedback Directed Program Restructuring](http://www.research.ibm.com/haifa/projects/systems/cot/fdpr/) (FDPR) is a post-link optimization tool for Linux on Power.  The tool has a few phases:  instrument, profile, and optimize.  All of these steps are performed after compilation and linking, working directly with the application binary executables and libraries.  In addition, the tool can produce a report ("journal") indicating performance issues detected, location in the source code, and likely remedies.

This project provides scripts which make the most common uses of FDPR trivially easy.

## Contributing to the project
We welcome contributions to the FDPR-Wrap Project in many forms. There's always plenty to do! Full details of how to contribute to this project are documented in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Maintainers
The project's [maintainers](MAINTAINERS.txt) are responsible for reviewing and merging all pull requests and they guide the overall technical direction of the project.

## Communication <a name="communication"></a>
We use [Slack](https://toolsforpower.slack.com/) for communication.

## Supported Architecture and Operating Systems
ppc64le: Ubuntu 16.04, CentOS7, RHEL 7, SLES12, Fedora 25.

## Building

```
$ git clone https://github.com/open-power-sdk/fdpr-wrap.git
$ cd fdpr-wrap
$ make
```

## Installing

One can simply install the built RPMs (as root):
`# rpm -i fdpr_wrap-_version_.rpm`

Official RPMs and DEBs can be downloaded from the [IBM Linux on Power Developer Portal](https://developer.ibm.com/linuxonpower/sdk-packages/).

## Documentation

- `fdpr_instr`

  **Intruments** the given binary in preparation for profiling, producing a new `_program_.instr` binary.

  Basic usage: `fdpr_instr _program_`

- `fdpr_instr_prof`

  **Intruments** the given binary in preparation for profiling, producing a new `_program_.instr` binary, and
  **Profiles** the instrumented application, producing a `_program_.prof` data file.

  Basic usage: `fdpr_instr_prof _program_ _[args]_`

- `fdpr_instr_prof_jour`

  **Intruments** the given binary in preparation for profiling, producing a new `_program_.instr` binary, and
  **Profiles** the instrumented application, producing a `_program_.prof` data file, and an **issues report** in `_program_jour.xml`.

  Basic usage: `fdpr_instr_prof_jour _program_ _[args]_`

- `fdpr_instr_prof_opt`

  **Intruments** the given binary in preparation for profiling, producing a new `_program_.instr` binary, and
  **Profiles** the instrumented application, producing a `_program_.prof` data file, and
  **Optimizes** the binary, producing a new `_program_.fdpr` optimized binary.

  Basic usage: `fdpr_instr_prof_opt _program_ _[args]_`

- `fdpr_jour`

  Produces a `_program_jour.xml` **issues report** based on an existing `_program_.prof` data file.

  Basic usage: `fdpr_jour _program_`

- `fdpr_opt`

  **Optimizes** a binary based on an existing `_program_.prof` data file, producing a new `_program_.fdpr` optimized binary.

  Basic usage: `fdpr_opt _program_`

- `fdpr_prof`

  **Profiles** an existing `_program_.instr` instrumented application, producing a `_program_.prof` data file.

  Basic usage: `fdpr_prof _program_ _[args]_`

- `fdpr_prof_jour`

  **Profiles** an existing `_program_.instr` instrumented application, producing a `_program_.prof` data file, and an **issues report** in `_program_jour.xml`.

  Basic usage: `fdpr_prof_jour _program_ _[args]_`

- `fdpr_prof_opt`

  **Profiles** an existing `_program_.instr` instrumented application, producing a `_program_.prof` data file, and
  **Optimizes** the binary, producing a new `_program_.fdpr` optimized binary.

  Basic usage: `fdpr_prof_opt _program_ _[args]_`

## Still Have Questions?
For general purpose questions, please use [StackOverflow](http://stackoverflow.com/questions/tagged/toolsforpower).

## License <a name="license"></a>
The FDPR-Wrap Project uses the [Apache License Version 2.0](LICENSE) software license.

## Related information
IBM's [Feedback Directed Program Restructuring](http://www.research.ibm.com/haifa/projects/systems/cot/fdpr/) (FDPR)
