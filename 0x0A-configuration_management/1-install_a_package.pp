# Define package resource to install Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',    # Ensuring specific version
  provider => 'pip3',     # Using pip3 provider
}
