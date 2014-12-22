Name:           libunistring
Version:        0.9.4
Release:        0
License:        LGPL-3.0+ and GPL-3.0+
Summary:        GNU Unicode string library
Url:            http://www.gnu.org/software/libunistring/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source1001:     libunistring.manifest

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package devel
Summary:        GNU Unicode string library - development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       info

%description devel
Development files for programs using libunistring and documentation
for UniString library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static --disable-rpath --docdir=%_docdir/%{name}
%__make %{?_smp_mflags}

%check
%if ! 0%{?qemu_user_space_build}
%__make check %{?_smp_mflags}
%endif

%install
echo " " > debugsources.list
%make_install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libunistring.la


%remove_docs

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libunistring.so.2*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libunistring.so
%{_includedir}/unistring
%{_includedir}/*.h
