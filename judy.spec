%define	major 1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	A general purpose dynamic array implemented as a C callable library
Name:		judy
Version:	1.0.5
Release:	%mkrel 3
Group:		System/Libraries
License:	LGPL
URL:		http://sourceforge.net/projects/judy/
Source0:	http://downloads.sourceforge.net/project/judy/judy/Judy-%{version}/Judy-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Static library and header files for the libjudy library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
Judy is a general purpose dynamic array implemented as a C callable library.
Judy's speed and memory usage are typically better than other data storage
models and improves with very large data sets.

%prep

%setup -q

%build
rm -rf autom4te.cache
rm -f configure
autoreconf -fi

%configure2_5x

make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.*a
%{_mandir}/man3/*

