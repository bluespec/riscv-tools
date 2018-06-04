%global release_num 20170602+2
%global prefix /opt/riscv32-unknown-elf-rv32im

Name: riscv-gnu-toolchain
Version: %{release_num}
Release: 1%{?dist}
Summary: Toolchain for RISC-V
License: GPL2
Group: Development/Tools/Other
Source0: %{name}_%{release_num}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
#Requires:  #todo
BuildRequires: redhat-rpm-config, rpm-build, autoconf, automake, libmpc-devel, mpfr-devel, gmp-devel, gawk, bison, flex, texinfo, patchutils, gcc, gcc-c++, zlib-devel, make, curl, python-devel
%{?el6:BuildRequires: devtoolset-3-gcc, devtoolset-3-gcc-c++}

%description
This package contains the source for the RISC-V toolchain.

%package -n riscv32-unknown-elf-rv32im
Summary: Toolchain for the riscv32-unknown-elf target, rv32im variant
Group: Development/Tools/Other
%description -n riscv32-unknown-elf-rv32im
This package contains a development toolchain for RISC-V.  This
package contains the riscv32-unknown-elf toolchain, targeting bare
metal application with the Newlib C library.
.
The hardware targeted by this toolchain is version 2.1 of the User
Level ISA, variant RV32IM.  In addition, the Privileged Architecture
version 1.10 is supported.

%prep
%autosetup -n riscv-gnu-toolchain-packaging

%build
# should probably be part of %clean
rm -rf %{prefix}
rm -rf %{buildroot}%{_bindir}/riscv32-*

./configure --with-arch=rv32im --prefix=%{prefix}
make
mkdir -p %{buildroot}/opt/
cp -a %{prefix} %{buildroot}/opt/

mkdir -p %{buildroot}%{_bindir}/
for f in %{buildroot}%{prefix}/bin/*; do
    b=`basename $f`
    ln -s %{prefix}/bin/$b %{buildroot}%{_bindir}/
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
%{_bindir}/riscv32-unknown-elf-*

%changelog
* Fri Jul 14 2017  Darius Rad <darius@bluespec.com>

- Update packaged version.

* Wed Jun 28 2017  Darius Rad <darius@bluespec.com>

- Initial version.
