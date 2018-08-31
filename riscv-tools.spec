%global release_num 20180620+3
%global prefix32 /opt/riscv32-unknown-elf-rv32im
%global prefix64 /opt/riscv64-unknown-elf-rv64im

Name: riscv-tools
Version: %{release_num}
Release: 1%{?dist}
Summary: Tools for the riscv{32,64}-unknown-elf target, rv32im and rv64im variants
License: GPL2
Group: Development/Tools/Other
Source0: %{name}_%{release_num}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
#Requires:  #todo
BuildRequires: redhat-rpm-config, rpm-build, autoconf, automake, libmpc-devel, mpfr-devel, gmp-devel, gawk, bison, flex, texinfo, patchutils, gcc, gcc-c++, zlib-devel, make, curl, python-devel, expat-devel
%{?el6:BuildRequires: devtoolset-3-gcc, devtoolset-3-gcc-c++}

%description
This package contains development tools for RISC-V.  This package
contains the riscv32-unknown-elf and riscv64-unknown-elf toolchains,
targeting bare metal applications with the Newlib C library.
.
The hardware targeted by these tools is version 2.1 of the User Level
ISA, variant RV32IM and RV64IM.  In addition, the Privileged
Architecture version 1.10 is supported.

%prep
%autosetup -n riscv-tools-packaging

%build
# should probably be part of %clean
rm -rf %{prefix32}
rm -rf %{prefix64}
rm -rf %{buildroot}%{_bindir}/riscv32-*
rm -rf %{buildroot}%{_bindir}/riscv64-*
rm -rf %{buildroot}%{_bindir}/openocd

(mkdir build-rv32 && cd build-rv32 && ../riscv-gnu-toolchain/configure --with-arch=rv32im --prefix=%{prefix32})
(mkdir build-rv64 && cd build-rv64 && ../riscv-gnu-toolchain/configure --with-arch=rv64im --prefix=%{prefix64} --with-cmodel=medany)
(cd riscv-openocd && ./configure --with-arch=rv64im --prefix=%{prefix32} --enable-remote-bitbang --enable-jtag_vpi --disable-werror)
make -C build-rv32
make -C build-rv64
make -C riscv-openocd
make -C build-rv32 install
make -C build-rv64 install
make -C riscv-openocd install
mkdir -p %{buildroot}/opt/
cp -a %{prefix32} %{buildroot}/opt/
cp -a %{prefix64} %{buildroot}/opt/

mkdir -p %{buildroot}%{_bindir}/
for f in %{buildroot}%{prefix32}/bin/*; do
    b=`basename $f`
    ln -sf %{prefix32}/bin/$b %{buildroot}%{_bindir}/
done
for f in %{buildroot}%{prefix64}/bin/*; do
    b=`basename $f`
    ln -sf %{prefix64}/bin/$b %{buildroot}%{_bindir}/
done

# fix links to buildroot
for f in %{buildroot}%{prefix32}/share/* %{buildroot}%{prefix64}/share/*; do
    if [ -L "$f" ]; then
	newtgt=`readlink $f | sed -e "s|^%{buildroot}||"`
	ln -sf "$newtgt" $f
    fi
done

%files
%{prefix32}
%{prefix64}
%{_bindir}/*

%changelog
* Fri Aug 31 2018  Darius Rad <darius@bluespec.com>

- Add rv64 tools and OpenOCD.

* Mon Jun 04 2018  Darius Rad <darius@bluespec.com>

- Initial version.
