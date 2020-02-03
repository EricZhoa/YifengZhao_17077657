/*
Write queries to answer the following questions
Save your work to this .sql file
Right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, FirstName, LastName, Title FROM Employee WHERE Title like '%IT%';

--2. List the names of all Artists and the titles of their albums
SELECT Artist.Name, Album.Title
FROM Artist
        JOIN Album ON Album.ArtistId = Artist.ArtistId;

--3. Which track is features on the greatest number of times in playlists and how many times is it included? (display Trac
SELECT Track.Name, count(Track.Name)
FROM Playlist
        JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId
        JOIN Track ON Track.TrackId = PlaylistTrack.TrackId
GROUP BY Track.Name
ORDER BY count(Track.Name) DESC
LIMIT 1

--4. Provide a list of the number of tracks by each artist
SELECT Artist.Name, MAX(Track.AlbumId) AS Tracks
FROM Album
        JOIN Track ON Track.AlbumId = Album.AlbumId
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
GROUP BY Artist.Name;

--5. How much money has been invoiced for the artist Deep Purple? (display each line item from the invoices and the total amount)
SELECT DeepPurple.Name,SUM(Invoice.Total) AS MoneyInvoiced
FROM Invoice
        JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
        JOIN Track ON Track.TrackId = InvoiceLine.TrackId
        JOIN Album ON Album.AlbumId = Track.AlbumId
        JOIN Artist DeepPurple ON Album.ArtistId = DeepPurple.ArtistId
WHERE DeepPurple.Name = 'Deep Purple';