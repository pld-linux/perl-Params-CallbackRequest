#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	CallbackRequest
Summary:	Params::CallbackRequest - Functional and object-oriented callback architecture
#Summary(pl):	
Name:		perl-Params-CallbackRequest
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69183af032eebccd5a7d734ab084b823
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exception::Class) >= 1.1
BuildRequires:	perl(Params::Validate) >= 0.59
BuildRequires:	perl(Test::Simple) >= 0.17
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::CallbackRequest provides functional and object-oriented callbacks
to method and function parameters. Callbacks may be either code references
provided to the C<new()> constructor, or methods defined in subclasses
of Params::Callback. Callbacks are triggered either for every call to
the Params::CallbackRequest C<request()> method, or by specially named
keys in the parameters to C<request()>.

# %description -l pl
# TODO

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
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
