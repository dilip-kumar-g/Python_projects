-- TABLE
CREATE TABLE Artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthdate DATE,
    bio TEXT
    -- other fields as needed
);
CREATE TABLE Artist_Roles (
    artist_id INTEGER,
    movie_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (artist_id, movie_id, role_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);
CREATE TABLE Artist_Skills (
    artist_id INTEGER,
    skill_id INTEGER,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);
CREATE TABLE Genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE Media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    type TEXT, -- Change ENUM('Video', 'Image') to TEXT or VARCHAR
    url TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);
CREATE TABLE Movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_date DATE,
    duration INTEGER,
    director TEXT,
    -- other fields as needed
    UNIQUE(title) -- Example of a unique constraint
);
CREATE TABLE Movie_Genres (
    movie_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);
CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    user_id INTEGER, -- Assuming there's a Users table
    rating DECIMAL(3,1),
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE Skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
