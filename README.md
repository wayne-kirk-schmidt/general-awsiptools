AWS Ip Tools
============

Sometimes it's nice to see how much AWS IP space extends to help configure firewalls and so on.
The tools in this repository will operate on the AWS IP ranges JSON file:

[IP-Json-File](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html)

Usage
=====


Expand out all of the IP network address blocks into specific IP Addresses.

+   ./bin/awsparser.ip-addresses.py <jsonfile>

Parse out network blocks:

+   ./bin/awsparser.ip-networks.py

License
=======

Copyright 2022 Wayne Kirk Schmidt
https://www.linkedin.com/in/waynekirkschmidt

Licensed under the Apache 2.0 License (the "License");

You may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   APACHE 2.0
    license-url    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: 

+   wschmidt@sumologic.com

+   wayne.kirk.schmidt@gmail.com

I will provide "best effort" fixes and extend the scripts.
