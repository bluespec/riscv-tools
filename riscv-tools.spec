%global release_num 20180620+2
%global prefix /opt/riscv32-unknown-elf-rv32im

Name: riscv-tools
Version: %{release_num}
Release: 1%{?dist}
Summary: Tools for RISC-V
License: GPL2
Group: Development/Tools/Other
Source0: %{name}_%{release_num}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
#Requires:  #todo
BuildRequires: redhat-rpm-config, rpm-build, autoconf, automake, libmpc-devel, mpfr-devel, gmp-devel, gawk, bison, flex, texinfo, patchutils, gcc, gcc-c++, zlib-devel, make, curl, python-devel, expat-devel
%{?el6:BuildRequires: devtoolset-3-gcc, devtoolset-3-gcc-c++}

%description
This package contains the source for the RISC-V tools.

%package -n riscv32-unknown-elf-rv32im
Summary: Tools for the riscv32-unknown-elf target, rv32im variant
Group: Development/Tools/Other
%description -n riscv32-unknown-elf-rv32im

This package contains development tools for RISC-V.  This package
contains the riscv32-unknown-elf toolchain, targeting bare metal
application with the Newlib C library.
.
The hardware targeted by these tools is version 2.1 of the User Level
ISA, variant RV32IM.  In addition, the Privileged Architecture version
1.10 is supported.

%prep
%autosetup -n riscv-tools-packaging

%build
# should probably be part of %clean
rm -rf %{prefix}
rm -rf %{buildroot}%{_bindir}/riscv32-*

(cd riscv-gnu-toolchain && ./configure --with-arch=rv32im --prefix=%{prefix})
(cd riscv-openocd && ./configure --with-arch=rv32im --prefix=%{prefix} --enable-remote-bitbang --enable-jtag_vpi --disable-werror)
make -C riscv-gnu-toolchain
make -C riscv-openocd
make -C riscv-gnu-toolchain install
make -C riscv-openocd install
mkdir -p %{buildroot}/opt/
cp -a %{prefix} %{buildroot}/opt/

mkdir -p %{buildroot}%{_bindir}/
for f in %{buildroot}%{prefix}/bin/*; do
    b=`basename $f`
    ln -sf %{prefix}/bin/$b %{buildroot}%{_bindir}/
done

# fix links to buildroot
for f in %{buildroot}%{prefix}/share/*; do
    if [ -L "$f" ]; then
	newtgt=`readlink $f | sed -e "s|^%{buildroot}||"`
	ln -sf "$newtgt" $f
    fi
done

%files
%{prefix}
%{_bindir}/*

%changelog
* Mon Jun 04 2018  Darius Rad <darius@bluespec.com>

- Initial version.
