def test_jenkins_is_installed(host):
    jenkins = host.package("jenkins")
    assert jenkins.is_installed
    assert jenkins.version.startswith("2.1")