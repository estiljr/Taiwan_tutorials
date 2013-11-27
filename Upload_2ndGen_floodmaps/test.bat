
set INFILES="C:\isis\data\examples\ISIS 2D\Site 1\GIS\Dam_Active_Area.shp"
::for %%F in (%INFILES%) do set NAME=%%~nF
::set RP=%INFILES:~-5,1%
::echo %RP%

set LAYERNAME="temp_gi.second_gen_flood_maps"

setlocal EnableDelayedExpansion
for /D %%I in (%INFILES%) do (
set k=%%I
set RP=!k:~-8,4%!
echo !RP!
REM ogr2ogr -f PostgreSQL PG:"dbname=taiwan host=localhost port=5432 user=taiwan_user password=taiwan" %%I -nln %LAYERNAME% -nlt POLYGON -lco FID=gid -lco GEOMETRY_NAME=geom -s_srs EPSG:3826 -a_srs EPSG:3826 -sql "SELECT '%%~nI' as NAME, CLASS as class, '!RP!' as rp, '' as duration FROM '%%~nI'" -append

ogr2ogr -f PostgreSQL PG:"dbname=taiwan host=localhost port=5432 user=taiwan_user password=taiwan" %%I -nln %LAYERNAME% -nlt POLYGON
)
::psql -d taiwan -h localhost -U taiwan_user -c "VACUUM ANALYSE %LAYERNAME%"