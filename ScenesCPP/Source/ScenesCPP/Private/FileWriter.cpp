// Fill out your copyright notice in the Description page of Project Settings.


#include "FileWriter.h"

#include "Misc/FileHelper.h"
#include "HAL/PlatformFilemanager.h"

bool UFileWriter::SaveStringToFile(const FString& FilePath, const FString& Text)
{
    return FFileHelper::SaveStringToFile(Text, *FilePath);
}

