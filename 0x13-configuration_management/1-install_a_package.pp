#This puppet manifest installs puppet-lint
package { 'puppet-lint':
ensure   => 'latest',
provider => 'gem'
}