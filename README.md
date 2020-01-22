Replicating a Django F reference issue with check constraints

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -e ~/path/to/django
$ python manage.py sqlmigrate core 0002
BEGIN;
--
-- Create constraint percentages_sum_100 on model book
--
CREATE TABLE "new__core_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "percent_read" integer unsigned NOT NULL CHECK ("percent_read" >= 0), "percent_unread" integer unsigned NOT NULL CHECK ("percent_unread" >= 0), "percent_ignored" integer unsigned NOT NULL CHECK ("percent_ignored" >= 0), CONSTRAINT "percentages_sum_100" CHECK ("percent_read" = ((100 - "new__core_book"."percent_unread") - "new__core_book"."percent_ignored")));
INSERT INTO "new__core_book" ("id", "percent_read", "percent_unread", "percent_ignored") SELECT "id", "percent_read", "percent_unread", "percent_ignored" FROM "core_book";
DROP TABLE "core_book";
ALTER TABLE "new__core_book" RENAME TO "core_book";
COMMIT;
$ python manage.py migrate
...
django.db.utils.DatabaseError: malformed database schema (core_book) - no such column: new__core_book.percent_unread
```
