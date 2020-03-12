#!/usr/bin/perl -Tw

use strict;
use CGI;

my($cgi) = new CGI;

print $cgi->header;
my($message) = " ";
$message = $cgi->param('message') if defined $cgi->param('message');

#print $cgi->start_html(-title => uc($color),
   #                    -BGCOLOR => $color);
print $cgi->h1("Your input message is: $message");
print $cgi->end_html;
