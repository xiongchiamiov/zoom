CREATE TABLE redirects (
    -- In SQLite, all characters types end up as TEXT, so we're just declaring
    -- it that way to start, rather than being misleading about using
    -- VARCHAR(255) or whatever.
    id TEXT primary key not null,
    url TEXT not null
);
