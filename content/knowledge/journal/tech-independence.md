---
date: 2025-02-15
title: Building Your Own Cloud
categories: ["Tech", "Self-Hosting"]
tags: ["nextcloud", "privacy"]
type: docs
summary: "How to set up your own iCloud replacement with a cloud CPU that you own."
status: seedling

---

I’ve always enjoyed the DIY life. And this experiment is around creating my own cloud that I own. I’ve used iCloud for years and years, and I wanted to see if I could have a go at it on my own.

This is inspired by Derek Sivers’ [Tech Independence](https://sive.rs/ti) post. I got my start there, but realized I wasn’t comfortable with OpenBSD in the same way I was Ubuntu, and I wanted to do a few other things, so I modified those directions.

## Before You Begin

A few tips for you:
- It’s worth it to set this up and let it run for a few weeks before totally leaving your old cloud platform. You don’t want to risk data loss.
- You should definitely back up your files. 
- If you’re new to working in the command line, the app you use is called Terminal if you’re on macOS.
- Any time you see `~`, it’s a shortcut to your user folder.
	- On Mac/Linux, ~ replaces /Users/YourName/.
	- On Ubuntu servers, it’s less relevant because you’re managing Nextcloud as root. But if you switch users (joshuagraves), ~ refers to /home/joshuagraves/.

## Generate an SSH Key Before Deploying the Server

To securely connect to your server without passwords, generate an SSH key before creating your server.

Generate an SSH key on your machine:

```
ssh-keygen -t ed25519 -C "your-email@example.com"
```
- Save it when prompted (default: `~/.ssh/id_ed25519`).
- No passphrase is required (optional for added security).

Add the SSH Key to Vultr Before Deploying the Server:
- Go to Vultr Dashboard → Account → SSH Keys.
- Click Add SSH Key.
- Copy and paste the contents of `~/.ssh/id_ed25519.pub`.

## Deploy a Vultr Server & Attach Block Storage

Now, you'll create a new server.

1.	Go to Vultr → Deploy a New Instance.
2.	Choose: 
	- Ubuntu 22.04 LTS
	- One-Click Nextcloud (DO NOT use Snap—Snap limits control over Nextcloud, like thumbnail generation).
	- Shared CPU Plan (best price-performance balance).
	- Enable backups (Vultr charges extra, but it’s worth it—you will screw up at some point).
	- Attach your SSH key (so you can log in without a password).
3.	Once deployed, note:
	- Public IP Address
	- Initial Nextcloud Admin Username & Password (from Vultr panel)
	- Root SSH Access (via SSH key)

## Create and Attach Block Storage

The default storage on Vultr instances is small. If you want to store photos, music, or large files, you need block storage.

1.	Go to Vultr → Block Storage → Add Volume.
2.	Choose:
	- SSD (not NVMe) (NVMe is more expensive and usually unnecessary).
	- Go bigger than you think you need (you CANNOT downsize block storage later).
	- Attach it to the Nextcloud server you just created.
	- Enable backups for block storage (extra cost but crucial for safety).

## Access Your Server via SSH

Use SSH to access your server securely:

```
ssh root@<SERVER_IP>
```

This connects you using the SSH key you added earlier.

To mount block storage, you need to attach the block storage so Nextcloud uses it for data.

Find your block storage by running:

```
lsblk
```

Look for your disk (mine was 500GB, so it appeared as):

```
vdb    252:16   0  500G  0 disk
└─vdb1 252:17   0  500G  0 part
```

Now, you'll format the block storage, but ONLY if it’s new.

{{< hint warning >}}
**WARNING: This will wipe all data! Skip if it contains files.**
{{< /hint >}}

Unless you changed something, `vdb1` is your volume name. Run:

```
sudo mkfs.ext4 /dev/vdb1
```

Now you'll mount your block storage:

```
sudo mkdir -p /mnt/blockstorage
sudo mount /dev/vdb1 /mnt/blockstorage
```

You'll want to make the system load this when it boots up so you don't have to attach it each time. Run:

```
sudo nano /etc/fstab
```

In the file, add the following line:

```
UUID=$(blkid -s UUID -o value /dev/vdb1) /mnt/blockstorage ext4 defaults,nofail 0 0
```

Press `CTRL + X` to save and apply it. Then run:

```
sudo mount -a
```

## Configure Nextcloud to Use Block Storage for Data

Now we’ll point Nextcloud to use this directory. Run:

```
sudo mv /var/www/html/data /mnt/blockstorage/nextcloud-data
```

You'll create what's called a symlink (sometimes known as symbolic link or alias) to the new data directory by running:

```
sudo ln -s /mnt/blockstorage/nextcloud-data /var/www/html/data
```

Now that you've linked it, you want to add it to Nextcloud's config file. Run:

```
sudo nano /var/www/html/config/config.php
```

In the file, look for `datadirectory`. Change it to your storage location:

```
'datadirectory' => '/mnt/blockstorage/nextcloud-data',
```

Now that Nextcloud can see block storage, it needs write access. Run this, which grants it and any new files the proper permission.

```
sudo chown -R www-data:www-data /mnt/blockstorage/nextcloud-data
sudo chmod -R 750 /mnt/blockstorage/nextcloud-data
sudo chmod g+s /mnt/blockstorage/nextcloud-data
```

For good measure, restart Nginx & PHP:

```
sudo systemctl restart nginx
sudo systemctl restart php8.1-fpm
```

## Configure Trusted Domains
This lets you access your nextcloud from your domain. Run this:

```
sudo nano /var/www/html/config/config.php
```

Look for 'trusted_domains' and modify it like the below example. It's likely that it has `0 => your-server-ip`. So go to the next line and add your domain:

```
'trusted_domains' => array (
    0 => 'your-server-ip',
    1 => 'your-domain.com',
),
```

Secure your server with Let’s Encrypt SSL. It's free and a good security practice. Run: 

	sudo apt update && sudo apt install certbot python3-certbot-nginx -y
	sudo certbot --nginx -d your-domain.com

Make sure to enable auto-renewal, too! You'll make a cronjob, which has your system run a command every so often. Run:

	sudo crontab -e

Add this line to the bottom:

	0 3 * * * certbot renew --quiet

## Create a New User with Full Access

For security, create a non-root user. Trust me, do it. It's worth it.

	sudo adduser joshuagraves
	sudo usermod -aG sudo joshuagraves
	sudo chown -R joshuagraves:joshuagraves /mnt/blockstorage
	sudo chmod -R 770 /mnt/blockstorage
	sudo chmod g+s /mnt/blockstorage

## Transfer Files Efficiently

There are a few ways to get files into Nextcloud. One is by the web interface, which is fine. But sometimes it's clunky and slow. If you can learn `rsync` and `wget` you'll be in much better shape, as these run faster than the web interface does.

To use `rsync`, do this:

	rsync -ahv --progress -e "ssh" ~/Path/To/File joshuagraves@<SERVER_IP>:/mnt/blockstorage/nextcloud-data/YourUserID/files/Documents

The first path is where your file is locally. The second is a command to log in via SSH for the non-root user we created and place it in a specified directory.

You can also use `wget` if there are files already accessible online. This doesn't work with iCloud, or any other cloud drive that I've found. But if you have files on another server you own, this is the ticket:

	cd /mnt/blockstorage/nextcloud-data/YourUserID/files/
	wget <file-url>

## Rescan Files in Nextcloud

It's likely that you've uploaded a ton of files. It might've taken a while. For good measure, tell Nextcloud to detect new files:

	sudo -u www-data php /var/www/html/occ files:scan --all

This can take a while. Mine went 10 minutes.

## Troubleshooting Permissions Issues

During setup, I had to update permissions multiple times. If you encounter errors like:
- “Your data directory is invalid.”
- “Target directory doesn’t exist.”
- “Permission denied when uploading files.”

It means Nextcloud can’t write to these directories or something got wonky. Try running these commands:

To ensure the correct owner and group:
```
sudo chown -R www-data:www-data /mnt/blockstorage/nextcloud-data
```

To ensure the correct permissions:
```
	sudo chmod -R 750 /mnt/blockstorage/nextcloud-data
	sudo chmod g+s /mnt/blockstorage/nextcloud-data
```

To restart services:
```
sudo systemctl restart nginx
sudo systemctl restart php8.1-fpm
```

If you are moving large files manually via rsync or wget, rescan Nextcloud’s file system after fixing permissions:

	sudo -u www-data php /var/www/html/occ files:scan --all

This should resolve most issues with files not appearing, permission errors, or Nextcloud not recognizing new uploads.

## Afterword

Nextcloud is a great self-hosted alternative to iCloud, Google Drive, or Dropbox. There's a healthy ecosystem of free open source apps, like calendar, contacts, and mail to expand its functionality. It's also got a task tracker.

You’ll want to make sure to read up on how to do maintenance, but for now, go into Nextcloud’s Administration Settings and set your updates to auto. 

Have fun!