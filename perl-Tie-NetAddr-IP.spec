#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	NetAddr-IP
Summary:	Tie::NetAddr::IP - Implements a Hash where the key is a subnet
Summary(pl):	Tie::NetAddr::IP - implementacja hasza z podsieci± jako kluczem
Name:		perl-Tie-NetAddr-IP
Version:	1.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	562a9e63cc3e0cf0803778922f285ff8
URL:		http://search.cpan.org/dist/Tie-NetAddr-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-NetAddr-IP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module overloads hashes so that the key can be a subnet as in
NetAddr::IP. When looking values up, an interpretation will be made to
find the given key within the subnets specified in the hash.

%description -l pl
Ten modu³ przeci±¿a tablice asocjacyjne tak, ¿e klucz mo¿e byæ
podsieci± tak± jak w NetAddr::IP. Przy wyszukiwaniu warto¶ci
interpreter wyszuka podany klucz w podsieciach zdefiniowanych w haszu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tie/NetAddr
%{_mandir}/man3/*
