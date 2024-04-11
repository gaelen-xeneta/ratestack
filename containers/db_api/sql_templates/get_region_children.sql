WITH RECURSIVE region_children
AS (
    SELECT slug
        FROM regions
        WHERE slug = '{slug}'
    UNION
    SELECT r.slug
        FROM regions r
        INNER JOIN region_children c ON c.slug = r.parent_slug
)
SELECT * FROM region_children;
