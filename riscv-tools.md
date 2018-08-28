% GNU Tools for RISC-V RV32IM
% Bluespec, Inc. <support@bluespec.com>
% 2018-08-28

<!--
  generate html with:
    pandoc -s -f markdown -t html -o riscv-tools.html riscv-tools.md
-->

This pages describes the OS packages of the GNU tools (binutils, gcc,
OpenOCD, etc.) targeting RISC-V RV32IM.

# Determine Your Operating System

The following operating systems are supported:

* Debian 9 (stretch)
* Debian 8 (jessie)
* Ubuntu 18.04 LTS (bionic)
* Ubuntu 16.04 LTS (xenial)
* Ubuntu 14.04 LTS (trusty)
* CentOS 7 / RedHat Enterprise Linux 7
* CentOS 6 / RedHat Enterprise Linux 6

Attempt to determine your operating system by running the following
command:

~~~sh
( . /etc/os-release && echo $PRETTY_NAME )
~~~

If the above commands report a meaningful description of your system,
such as:

~~~sh
Debian GNU/Linux 9 (stretch)
~~~

or

~~~sh
CentOS Linux 7 (Core)
~~~

Then that is the system you are running.  Continue to the next step,
**Determine Your Hardware Architecture,** below.

If running the above returned an error, such as `No such file or
directory`, continue with the following steps.

Run the following command:

~~~sh
cat /etc/redhat-release
~~~

If this produces a meaningful description of your system, then proceed
to the next step.

If none of the above commands provide a meaningful description of your
system, or the description does not approximately match the list of
supporting operating systems above, then your system is not currently
supported.

# Determine Your Hardware Architecture

The following hardware architectures are supported for all operating
systems listed above:

* Intel and AMD 64-bit (also known as amd64 or x86_64)
* Intel and AMD 32-bit (also known as i386, i686, or x86)

Determine the hardware architecture of your host by running the
following command:

~~~sh
uname -m
~~~

That should usually return something like `x86_64`, indicating 64-bit,
or `i686`, indicating 32-bit.

Note that this is the architecture of the host.  There are packages
for both 32-bit and 64-bit target architectures (RV32IM and RV64IM,
respectively).

# Download the Installation Package

Based on your operating system and architecture identified above,
download the package appropriate for your system from one of the links
below:

* Debian 9 (stretch)
    * [rv32im target on amd64 host](stretch/riscv32-unknown-elf-rv32im_20180620+3_amd64.deb)
    * [rv32im target on i386 host](stretch/riscv32-unknown-elf-rv32im_20180620+3_i386.deb)
    * [rv64im target on amd64 host](stretch/riscv64-unknown-elf-rv64im_20180620+3_amd64.deb)
    * [rv64im target on i386 host](stretch/riscv64-unknown-elf-rv64im_20180620+3_i386.deb)
* Debian 8 (jessie)
    * [rv32im target on amd64 host](jessie/riscv32-unknown-elf-rv32im_20180620+3_amd64.deb)
    * [rv32im target on i386 host](jessie/riscv32-unknown-elf-rv32im_20180620+3_i386.deb)
    * [rv64im target on amd64 host](jessie/riscv64-unknown-elf-rv64im_20180620+3_amd64.deb)
    * [rv64im target on i386 host](jessie/riscv64-unknown-elf-rv64im_20180620+3_i386.deb)
* Ubuntu 18.04 LTS (bionic)
    * [rv32im target on amd64 host](bionic/riscv32-unknown-elf-rv32im_20180620+3_amd64.deb)
    * [rv32im target on i386 host](bionic/riscv32-unknown-elf-rv32im_20180620+3_i386.deb)
    * [rv64im target on amd64 host](bionic/riscv64-unknown-elf-rv64im_20180620+3_amd64.deb)
    * [rv64im target on i386 host](bionic/riscv64-unknown-elf-rv64im_20180620+3_i386.deb)
* Ubuntu 16.04 LTS (xenial)
    * [rv32im target on amd64 host](xenial/riscv32-unknown-elf-rv32im_20180620+3_amd64.deb)
    * [rv32im target on i386 host](xenial/riscv32-unknown-elf-rv32im_20180620+3_i386.deb)
    * [rv64im target on amd64 host](xenial/riscv64-unknown-elf-rv64im_20180620+3_amd64.deb)
    * [rv64im target on i386 host](xenial/riscv64-unknown-elf-rv64im_20180620+3_i386.deb)
* Ubuntu 14.04 LTS (trusty)
    * [rv32im target on amd64 host](trusty/riscv32-unknown-elf-rv32im_20180620+3_amd64.deb)
    * [rv32im target on i386 host](trusty/riscv32-unknown-elf-rv32im_20180620+3_i386.deb)
    * [rv64im target on amd64 host](trusty/riscv64-unknown-elf-rv64im_20180620+3_amd64.deb)
    * [rv64im target on i386 host](trusty/riscv64-unknown-elf-rv64im_20180620+3_i386.deb)
* CentOS 7 / RedHat Enterprise Linux 7
    * [rv32im target on amd64 host](centos/riscv-tools-20180620+3-1.el7.x86_64.rpm)
    * [rv32im target on i386 host](centos/riscv-tools-20180620+3-1.el7.centos.i.i686.rpm)
* CentOS 6 / RedHat Enterprise Linux 6
    * [rv32im target on amd64 host](centos/riscv-tools-20180620+3-1.el6.x86_64.rpm)
    * [rv32im target on i386 host](centos/riscv-tools-20180620+3-1.el6.i686.rpm)

# Install the Package

In all of the instructions below, replace `<package>` with the name of
the local file that you downloaded in the previous step.  Note that
this must be the *local* file, not a URL.

The following steps must be performed as the root user.  If the `sudo`
application is installed, this may be done as follows:

~~~sh
sudo -s
~~~

`sudo` may prompt for a password, in which case it expects your *user*
password, not the root password.

If `sudo` fails, perhaps because it is not installed, an alternative
is to use `su` as follows:

~~~sh
su
~~~

`su` will prompt for the *root* password, not the user password.

Once you have successfully gained root privileges, either with `sudo`
or `su`, continue below with the section that matches your operating
system.

## Debian and Ubuntu, all versions

Run the following commands (as root, described above):

~~~sh
dpkg -i <package>
apt-get -f install
~~~

## CentOS and RedHat Enterprise Linux, all versions

Run the following commands (as root, described above):

~~~
yum install <package>
~~~

# Unsupported Systems

If your system is not supported above or you would otherwise like to
build the tools yourself, the source can be found on
github (<https://github.com/bluespec/riscv-tools/>).

The following steps will build tools similar to those in the packages
provided above:

~~~sh
git clone --recursive -b packaging https://github.com/bluespec/riscv-tools.git
cd riscv-tools
RISCV=/opt/riscv32-unknown-elf-rv32ima
./build-rv32ima.sh
~~~

# Further Information

Direct all questions or concerns to <support@bluespec.com>.
