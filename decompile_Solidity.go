package main

import (
	"context"
	"encoding/hex"
	"os/exec"

	"github.com/acarl005/stripansi"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethclient"
)

const MAINURL = "rpc url"

func decompiler() string {
	ctx := context.Background()

	web3, _ := ethclient.Dial(MAINURL)
	contractAddress := common.HexToAddress("0x93dd4a0b32b1e6495ec943d541a6f52e3cbcb834")

	xi, _ := web3.CodeAt(ctx, contractAddress, nil)
	encodedString := hex.EncodeToString(xi)

	// Bytecode decompiler
	cmd := exec.Command("panoramix", encodedString)
	res, _ := cmd.Output()
	cleanMsg := stripansi.Strip(string(res))

	return cleanMsg
}
