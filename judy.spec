%define	major	1
%define libname	%mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A general purpose dynamic array implemented as a C callable library
Name:		judy
Version:	1.0.5
Release:	15
Group:		System/Libraries
License:	LGPLv2
Url:		http://sourceforge.net/projects/judy/
Source0:	http://downloads.sourceforge.net/project/judy/judy/Judy-%{version}/Judy-%{version}.tar.gz
Patch0:		judy-automake-1.13.patch

%description
Judy is a general purpose dynamic array implemented as a C callable library.
Judy's speed and memory usage are typically better than other data storage
models and improves with very large data sets.

%package -n	%{libname}
Summary:	The shared libjudy library
Group:          System/Libraries

%description -n	%{libname}
Judy is a general purpose dynamic array implemented as a C callable library.
Judy's speed and memory usage are typically better than other data storage
models and improves with very large data sets.

%package -n	%{devname}
Summary:	Static library and header files for the libjudy library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{devname}
Judy is a general purpose dynamic array implemented as a C callable library.
Judy's speed and memory usage are typically better than other data storage
models and improves with very large data sets.

%prep
%setup -q
%autopatch -p1

rm -rf autom4te.cache
rm -f configure
autoreconf -fi

%build
%configure2_5x \
	--disable-static

make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libJudy.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

