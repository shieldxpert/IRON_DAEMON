# IRON DAEMON

![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Release](https://img.shields.io/badge/release-v2.0-orange?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/ShieldXpert/IRON_DAEMON?style=social)
![IRON DAEMON](https://github.com/shieldxpert/IRON_DAEMON/blob/main/banner.png)


IRON DAEMON is a lightweight and functional tool written in Python that enables the enumeration of SMB (Server Message Block) resources on Windows systems quickly, simply, and effectively. It is designed as a cybersecurity tool aimed at professionals in the field, forensic analysts, system administrators, and technical enthusiasts who need visibility into shared resources, users, groups, and operating systems present in a local network or audit environment.

The main focus of IRON DAEMON is operational simplicity without sacrificing technical capability. Unlike more complex tools that require multiple configurations, IRON DAEMON works directly from the console or by double-clicking (via an automated script), making it easy to integrate into analysis environments or use as a portable utility.

The tool automatically detects which SMB port (139 or 445) is open on the target system, first attempts an anonymous connection, and if that fails, prompts the user for valid credentials to authenticate. Once connected, it securely and cleanly gathers information, displaying available data without performing any intrusive or destructive actions.

IRON DAEMON does not brute-force passwords or exploit vulnerabilities. Its purpose is strictly passive and authenticated enumeration, based on SMB protocol capabilities and public libraries. This makes it an ethical tool that is compatible with corporate, educational, or research environments.

Key features include:
Automatic detection of open SMB ports (445 and 139)

Anonymous connection by default, with fallback to authentication

Enumeration of...

-Remote host name

-Operating system

-System users (if permitted)

-Local groups

-Shared SMB resources

-Compatible with Windows, Linux (via Samba), and virtualized environments

-Direct execution from terminal or using run.bat

-Clean, documented, and portable code

-IRON DAEMON is ideal for scenarios where a quick overview of a Windows network is required or to detect open configurations that may expose sensitive data through shared resources.

This project is released under the MIT License and has been developed by ShieldXpert as a tool for cybersecurity, network auditing, forensic analysis, and technical training in controlled environments.
