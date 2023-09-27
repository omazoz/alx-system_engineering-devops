# This installs flask
#Author: Oumayma Mazoz

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
