#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Params
%define		pnam	CallbackRequest
Summary:	Params::CallbackRequest - functional and object-oriented callback architecture
Summary(pl.UTF-8):	Params::CallbackRequest - architektura callbacków funkcyjnych i obiektowych
Name:		perl-Params-CallbackRequest
Version:	1.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ec47d6e9184435a5a826123b9aa1e5e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exception-Class >= 1.1
BuildRequires:	perl-Params-Validate >= 0.59
BuildRequires:	perl(Test::Simple) >= 0.17
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::CallbackRequest provides functional and object-oriented
callbacks to method and function parameters. Callbacks may be either
code references provided to the new() constructor, or methods defined
in subclasses of Params::Callback. Callbacks are triggered either for
every call to the Params::CallbackRequest request() method, or by
specially named keys in the parameters to request().

%description -l pl.UTF-8
Params::CallbackRequest dostarcza funkcyjne i zorientowane obiektowo
wywołania zwrotne (callbacki) dla parametrów metod i funkcji.
Callbacki mogą być referencjami do kodu przekazanymi do konstruktora
new(), albo metodami zdefiniowanymi w podklasach Params::Callback.
Wywołania zwrotne są wyzwalane albo dla każdego wywołania metody
request() klasy Params::CallbackRequest, albo przez specjalnie nazwane
klucze w parametrach dla request().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Params/*.pm
%{perl_vendorlib}/Params/CallbackRequest
%{_mandir}/man3/*
