await cursor.execute('INSERT INTO secretos VALUES (?,?,?)', (ctx.author.global_name, secreto))