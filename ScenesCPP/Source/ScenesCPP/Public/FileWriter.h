// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "FileWriter.generated.h"

/**
 * 
 */
UCLASS()
class SCENESCPP_API UFileWriter : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:
	UFUNCTION(BlueprintCallable, Category = "File")
		static bool SaveStringToFile(const FString& FilePath, const FString& Text);
};