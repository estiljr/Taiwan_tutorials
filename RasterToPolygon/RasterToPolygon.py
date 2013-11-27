def floodgrid_2_extent(in_grid,threshold,temp_grid,out_shp):

    import arcpy
    arcpy.CheckOutExtension("spatial")
    arcpy.env.scratchWorkspace =r"c:/temp/scratch"
    arcpy.env.overwriteOutput = True
    
    res = False
    try:
        arcpy.gp.GreaterThan_sa(in_grid, str(threshold), temp_grid)
        arcpy.RasterToPolygon_conversion(temp_grid, out_shp, "NO_SIMPLIFY", "VALUE")
        res = True
    except:
        print arcpy.GetMessages()
    finally:
        arcpy.CheckInExtension("spatial")
    
    return res

in_grid = r"C:\Projects\FM_Global\Taiwan\Data\2nd_Gen_FloodMaps\08_GIS_Changhua\grid_file_Changhua\changhua_i100"
out_shapefile = r"C:\Projects\FM_Global\Taiwan\Data\2nd_Gen_FloodMaps\08_GIS_Changhua\flood_extent\changhua_i0100.shp"
temp = r"c:/temp/scratch"
floodgrid_2_extent(in_grid, 0.01, temp, out_shapefile)