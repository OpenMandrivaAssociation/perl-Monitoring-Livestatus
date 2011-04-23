%define upstream_name    Monitoring-Livestatus
%define upstream_version 0.64

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Connector with multiple peers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Monitoring/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl(IO::Socket::UNIX)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Thread::Queue)
BuildRequires: perl(utf8)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module connects via socket/tcp to the check_mk livestatus addon for
Nagios and Icinga. You first have to install and activate the mklivestatus
addon in your monitoring installation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


