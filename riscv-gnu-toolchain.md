% GNU Toolchain for RISC-V RV32IM
% Bluespec, Inc. <support@bluespec.com>
% 2017-07-16

<!--
  generate html with:
    pandoc -s -f markdown -t html -o riscv-gnu-toolchain.html riscv-gnu-toolchain.md
-->

This pages describes the OS packages of the GNU toolchain (binutils,
gcc, etc.) targeting RISC-V RV32IM.

# Determine Your Operating System

The following operating systems are supported:

* Debian 9 (stretch)
* Debian 8 (jessie)
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

Note that this is the architecture of the host; all of the packages
provides tools for a 32-bit target architecture (i.e., RV32IM).

# Download the Installation Package

Based on your operating system and architecture identified above,
download the package appropriate for your system from one of the links
below:

* Debian 9 (stretch)
    * [64-bit](stretch/riscv32-unknown-elf-rv32im_20170602+2_amd64.deb)
    * [32-bit](stretch/riscv32-unknown-elf-rv32im_20170602+2_i386.deb)
* Debian 8 (jessie)
    * [64-bit](jessie/riscv32-unknown-elf-rv32im_20170602+2_amd64.deb)
    * [32-bit](jessie/riscv32-unknown-elf-rv32im_20170602+2_i386.deb)
* Ubuntu 16.04 LTS (xenial)
    * [64-bit](xenial/riscv32-unknown-elf-rv32im_20170602+2_amd64.deb)
    * [32-bit](xenial/riscv32-unknown-elf-rv32im_20170602+2_i386.deb)
* Ubuntu 14.04 LTS (trusty)
    * [64-bit](trusty/riscv32-unknown-elf-rv32im_20170602+2_amd64.deb)
    * [32-bit](trusty/riscv32-unknown-elf-rv32im_20170602+2_i386.deb)
* CentOS 7 / RedHat Enterprise Linux 7
    * [64-bit](centos/riscv-gnu-toolchain-20170602+2-1.el7.centos.x86_64.rpm)
    * [32-bit](centos/riscv-gnu-toolchain-20170602+2-1.el7.centos.i686.rpm)
* CentOS 6 / RedHat Enterprise Linux 6
    * [64-bit](centos/riscv-gnu-toolchain-20170602+2-1.el6.x86_64.rpm)
    * [32-bit](centos/riscv-gnu-toolchain-20170602+2-1.el6.i686.rpm)

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
build the toolchain yourself, the source can be found on
github (<https://github.com/riscv/riscv-gnu-toolchain/>).

The following steps will build tools similar to those in the packages
provided above:

~~~sh
git clone --recursive -b f5fae1c https://github.com/riscv/riscv-gnu-toolchain.git
cd riscv-gnu-toolchain
PATH=$PATH:/opt/riscv32-unknown-elf-rv32im/bin
./configure --with-arch=rv32im --prefix=/opt/riscv32-unknown-elf-rv32im
make
make install
~~~

# Further Information

Direct all questions or concerns to <support@bluespec.com>.
